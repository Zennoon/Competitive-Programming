class MyCircularDeque {
    int size;
    int maxsize;
    List<Integer> queue;

    public MyCircularDeque(int k) {
        this.maxsize = k;
        this.size = 0;
        this.queue = new ArrayList<>();
    }
    
    public boolean insertFront(int value) {
        if (! this.isFull()){
            this.queue.add(0, value);
            this.size += 1;
            return true;
        }
        return false;
    }
    
    public boolean insertLast(int value) {
        if (! this.isFull()){
            if (! this.isEmpty()){
                this.queue.add(this.size, value);
                this.size += 1;
                return true;
            }
            else {
                return this.insertFront(value);
            }
        }    
        return false;
    }
    
    public boolean deleteFront() {
        if (! this.isEmpty()){
            this.queue.remove(0);
            this.size -= 1;
            return true;
        }
        return false;
    }
    
    public boolean deleteLast() {
        if (! this.isEmpty()){
            this.queue.remove(this.size - 1);
            this.size -= 1;
            return true;
        }
        return false;
    }
    
    public int getFront() {
        if (! this.isEmpty()){
            return this.queue.get(0);
        }
        return -1;
    }
    
    public int getRear() {
        if (! this.isEmpty()){
            return this.queue.get(this.size - 1);
        }
        return -1;
    }
    
    public boolean isEmpty() {
        return this.size == 0;
    }
    
    public boolean isFull() {
        return this.size == this.maxsize;
    }
}
