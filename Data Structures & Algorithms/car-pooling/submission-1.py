class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        trips.sort(key = lambda pickup: pickup[1])
        # print(trips)
        
        last_trip = trips[0]
        current_capacity = capacity-last_trip[0]

        if current_capacity<0:
            return False

        for next_trip in trips[1:]:
            # print(f"last trip",last_trip)
            # print(f"nexct trip",next_trip)
            if next_trip[1]<last_trip[2]:
                # print(current_capacity)
                if current_capacity>=next_trip[0]:
                    current_capacity-=next_trip[0]
                else:
                    return False
            else:
                last_trip = next_trip
                current_capacity=capacity-next_trip[0]

        return True