const kue = require('kue')
  , queue = kue.createQueue();

const jobData = {
  phoneNumber: 'string',
  message: 'string',
};

const job = queue.create('push_notification_code', jobData).save(function (err) {
  if (!err) console.log(`Notification job created: ${job.id}`);
  })
  .on('complete', function () {
    console.log('Notification job completed');
  })
  .on('failed attempt', function (errorMessage, doneAttempts) {
    console.log('Notification job failed');
});
