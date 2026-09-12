class TimeMap:

    def __init__(self):
        self.store = {} #key=string, value=[list of [value, timestamp]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the key has not existed yet
        if key not in self.store:
            self.store[key] = []
        # Don't need to add duplicate timestamp
        if timestamp not in self.store[key]:
            self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # If key is found then the values holds the list of values from that key
        res, values = "", self.store.get(key, [])
        # Use binary search
        l, r = 0, len(values)-1

        while l <= r:
            mid = (l+r)//2      # integer division is //
            # If the value at middle index and the second value which is the timestamp 
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                # If timestamp is smaller than the given timestamp
                # We search the right side
                l = mid+1
            else:
                # Else we search the left side of the list
                r = mid-1

        return res