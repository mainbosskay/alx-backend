import { createQueue } from 'kue';

const notifyQueue = createQueue();

const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

notifyQueue.process('push_notification_code', (notifyJob, done) => {
  sendNotification(notifyJob.data.phoneNumber, notifyJob.data.message);
  done();
});
