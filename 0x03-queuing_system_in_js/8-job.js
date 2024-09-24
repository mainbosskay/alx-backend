const createPushNotificationsJobs = (jobs, queue) => {
  if (!(jobs instanceof Array)) {
    throw new Error('Jobs is not an array');
  }
  for (const jobsData of jobs) {
    const notifyJob = queue.create('push_notification_code_3', jobsData);

    notifyJob
      .on('enqueue', () => {
        console.log('Notification job created:', notifyJob.id);
      })
      .on('complete', () => {
        console.log('Notification job', notifyJob.id, 'completed');
      })
      .on('failed', (err) => {
        console.log('Notification job', notifyJob.id, 'failed:', err.message || err.toString());
      })
      .on('progress', (progress) => {
        console.log('Notification job', notifyJob.id, `${progress}% complete`);
      });
    notifyJob.save();
  }
};

export default createPushNotificationsJobs;
