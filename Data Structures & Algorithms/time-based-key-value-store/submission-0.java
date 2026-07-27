class TimeMap {
    Map<String, TreeMap<Integer,String>> hm;
    public TimeMap() {
        hm = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        if(hm.containsKey(key)){
            TreeMap<Integer,String> tm = hm.get(key);
            tm.put(timestamp,value);
            hm.put(key, tm);
        }else{
            TreeMap<Integer,String> tm = new TreeMap<>();
            tm.put(timestamp,value);
            hm.put(key, tm);
        }
    }
    
    public String get(String key, int timestamp) {
        if(!hm.containsKey(key)) return "";
        Integer val = hm.get(key).floorKey(timestamp);
        if(val == null) return  "";
        return hm.get(key).get(val);
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */