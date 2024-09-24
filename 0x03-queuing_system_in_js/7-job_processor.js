import { createQueue } from 'kue';

const blacklistPhoneNumbers = ['4153518780', '4153518781'];
const notifyQueue = createQueue();

const sendNotification = (phoneNumber, message, job, done) => {
  const totalAtms = 2; let pendingAtms = 2;
  const notifyInterval = setInterval(() => {
    if (totalAtms - pendingAtms <= totalAtms / 2) {
      job.progress(totalAtms - pendingAtms, totalAtms);
    }
    if (blacklistPhoneNumbers.includes(phoneNumber)) {
      done(new Error(`Phone number ${phoneNumber} is blacklisted`));
      clearInterval(notifyInterval);
      return;
    }
    if (totalAtms === pendingAtms) {
      console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    }
    pendingAtms -= 1;
    if (pendingAtms === 0) {
      done();
      clearInterval(notifyInterval);
    }
  }, 1000);
};

notifyQueue.process('push_notification_code_2', 2, (notifyJob, done) => {
  sendNotification(notifyJob.data.phoneNumber, notifyJob.data.message, notifyJob, done);
});
