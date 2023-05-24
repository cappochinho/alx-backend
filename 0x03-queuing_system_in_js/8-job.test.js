import createPushNotificationsJobs from './8-job.js';
const expect = require('chai').expect;

const kue = require('kue'),
  queue = kue.createQueue();

describe('createPushNotificationsJobs test suite', () => {
  before(() => queue.testMode.enter(true));
  afterEach(() => queue.testMode.clear());
  after(() => queue.testMode.exit());

  it('should throw an error if jobs is not an array', () => {

    expect(() => createPushNotificationsJobs("string", queue)).to.throw(Error, 'Jobs is not an array');
    expect(() => createPushNotificationsJobs({ key : "value" }, queue)).to.throw(Error, 'Jobs is not an array');
    expect(() => createPushNotificationsJobs(NaN, queue)).to.throw(Error, 'Jobs is not an array');
  }),

  it('Test if new job created for the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      }
    ];
    createPushNotificationsJobs(jobs, queue);
    queue.createJob('push_notification_code_3', jobs).save();
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data.phoneNumber).to.equal('4153518780');
    expect(queue.testMode.jobs[1].data).to.deep.equal({
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    })
  });
});
