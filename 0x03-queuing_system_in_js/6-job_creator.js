const jobData = {
  phoneNumber: '+233546938313',
  message: 'Edward Junior Agyemang-Prempeh',
}

const kue = require('kue');
let push_notification_code = kue.createQueue();

const notificationJob = push_notification_code.createJob(jobData);

notificationJob.on('enqueue', function() {
  console.log(`Notification job created: ${notificationJob.id}`);
});

notificationJob.on('complete', function() {
  console.log('Notification job completed');
});

notificationJob.on('failed', function() {
  console.log('Notification job failed');
});

notificationJob.save();
