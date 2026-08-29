class MyHashMap {
    int size;
    double y;
    static class HMNode{
        int key;
        int value;

        HMNode(int key,int value){
            this.key = key;
            this.value = value;
        }
    }

    private LinkedList<HMNode>[] buckets;

    public MyHashMap() {
        size = 0;
        init(4);
        y = 2;
    }

    private void init(int n){
        buckets = new LinkedList[n];
        for(int i = 0; i < n; i++){
            buckets[i] = new LinkedList<>();
        }
    }
    
    public void put(int key, int value) {
        int bi = getBucketInd(key);
        int di = getParticular(bi,key);

        if(di == -1){
            HMNode nnode = new HMNode(key,value);
            buckets[bi].add(nnode);
            size++;
        }else{
            buckets[bi].get(di).value = value;
        }

        double thre = size*1.0/buckets.length;

        if(thre >= y){
            rehash();
        }
    }

    private void rehash(){
        LinkedList<HMNode>[] nbuckets = buckets;
        size = 0;
        init(buckets.length*2);

        for(int i = 0; i < nbuckets.length; i++){
            for(int j = 0; j < nbuckets[i].size(); j++){
                put(nbuckets[i].get(j).key, nbuckets[i].get(j).value);
            }
        }
    }

    private int getBucketInd(int k){
        int hs = Integer.hashCode(k);
        int abshs = Math.abs(hs);
        return abshs%buckets.length;
    }
    
    private int getParticular(int idx,int key){
        LinkedList<HMNode> list = buckets[idx];
        int di = 0;
        for(int i = 0; i < list.size(); i++){
            if(list.get(i).key == key) return di;
            di++;
        }
        return -1;
    }

    public int get(int key) {
        int bi = getBucketInd(key);
        int di = getParticular(bi,key);

        if(di == -1){
            return -1;
        }else{
            return buckets[bi].get(di).value;
        }
    }
    
    public void remove(int key) {
        int bi = getBucketInd(key);
        int di = getParticular(bi,key);
        if(di == -1) return ;
        buckets[bi].remove(di);
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */