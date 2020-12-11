import queue
import threading

q = queue.Queue()

def worker(num):
    while True:
        item = q.get()
        if item is None:
            break
        # 작업을 처리한다.
        print("스레드 {0} : 처리 완료 {1}".format(num+1, item))
        q.task_done()

if __name__ == "__main__":
    num_worker_threads = 5
    threads = []
    for i in range(num_worker_threads):
        t = threading.Thread(target=worker, args=(i,))
        t.start()
        threads.append(t)

    for item in range(20):
        q.put(item)

    # 모든 작업이 끝날 때까지 대기한다(block).
    q.join()

    # 워커 스레드를 종료한다(stop).
    for i in range(num_worker_threads):
        q.put(None)
    for t in threads:
        t.join()