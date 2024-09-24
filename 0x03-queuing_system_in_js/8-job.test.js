import { createQueue } from 'kue';
import sinon from 'sinon';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';

describe('createPushNotificationsJobs', () => {
  const spyConsole = sinon.spy(console);
  const queue = createQueue({ name: 'push_notification_code_test' });

  before(() => {
    queue.testMode.enter(true);
  });

  after(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  afterEach(() => {
    spyConsole.log.resetHistory();
  });

  it('throws error when jobs is not an array', () => {
    expect(
      createPushNotificationsJobs.bind(createPushNotificationsJobs, {}, queue),
    ).to.throw('Jobs is not an array');
  });

  it('correctly adds jobs to the queue', (done) => {
    expect(queue.testMode.jobs.length).to.equal(0);
    const jobsData = [
      {
        phoneNumber: '123456789',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '987654321',
        message: 'This is the code 9876 to verify your account',
      },
    ];
    createPushNotificationsJobs(jobsData, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobsData[0]);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    queue.process('push_notification_code_3', () => {
      expect(
        spyConsole.log.calledWith('Notification job created:', queue.testMode.jobs[0].id),
      ).to.be.true;
      done();
    });
  });

  it('handles job progress events correctly', (done) => {
    queue.testMode.jobs[0].addListener('progress', () => {
      expect(
        spyConsole.log
          .calledWith('Notification job', queue.testMode.jobs[0].id, '25% complete'),
      ).to.be.true;
      done();
    });
    queue.testMode.jobs[0].emit('progress', 25);
  });

  it('handles job failure events correctly', (done) => {
    queue.testMode.jobs[0].addListener('failed', () => {
      expect(
        spyConsole.log
          .calledWith('Notification job', queue.testMode.jobs[0].id, 'failed:'),
      ).to.be.true;
      done();
    });
    queue.testMode.jobs[0].emit('failed', new Error('Failed to send'));
  });

  it('handles job completion events correctly', (done) => {
    queue.testMode.jobs[0].addListener('complete', () => {
      expect(
        spyConsole.log
          .calledWith('Notification job', queue.testMode.jobs[0].id, 'completed'),
      ).to.be.true;
      done();
    });
    queue.testMode.jobs[0].emit('complete');
  });
});
