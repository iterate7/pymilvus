import threading

from milvus.client.pool import ConnectionPool


class TestPool:
    def test_pool_max_conn(self):
        pool = ConnectionPool(uri="tcp://127.0.0.1:19530", pool_size=10)

        def run(_pool):
            conn = _pool.fetch()
            assert conn.conn_id() < 10
            conn.has_collection("test_pool")

        thread_list = []
        for _ in range(10 * 3):
            thread = threading.Thread(target=run, args=(pool,))
            thread.start()
            thread_list.append(thread)
