from Queue import Queue  
def test_empty():
    queue = Queue(5)
    assert queue.empty() == True

def test_full():
    queue = Queue(3)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.full() == True

def test_dequeue_empty():
    queue = Queue(5)
    assert queue.dequeue() is None

def test_dequeue():
    queue = Queue(5)
    queue.enqueue(7)
    queue.enqueue(4)
    queue.enqueue(5)
    assert queue.dequeue() == 7
    assert queue.dequeue() == 4

def test_enqueue():
    queue = Queue(3)
    assert queue.enqueue(7) == True
    assert queue.enqueue(4) == True
    assert queue.enqueue(5) == True
    assert queue.enqueue(6) == False

test_empty()
test_full()
test_dequeue_empty()
test_dequeue()
test_enqueue()

print("Todas las pruebas pasaron correctamente.")
