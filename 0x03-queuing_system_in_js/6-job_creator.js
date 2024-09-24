import { createQueue } from 'kue';

const notifyQueue = createQueue({ name: 'push_notification_code' });
const notifyJob = notifyQueue.create('push_notification_code', {
  phoneNumber: '08975644378',
  message: 'This is the verification of account code',
});

notifyJob
  .on('enqueue', () => {
    console.log('Notification job created:', notifyJob.id);
  })
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed', () => {
    console.log('Notification job failed');
  });
notifyJob.save();
