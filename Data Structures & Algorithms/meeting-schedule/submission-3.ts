/**
 * Definition of Interval:
 * class Interval  {
 *   constructor(start, end) {
 *     this.start = start;
 *     this.end = end;
 *   }
 * }
 */

class Solution {
    /**
     * @param {Interval[]} intervals
     * @returns {boolean}
     */
    canAttendMeetings(intervals: Interval[]): boolean {
        const sortedIntervals = intervals.sort((f, s) => f.start - s.start)
        
        for (var i = 0; i < sortedIntervals.length - 1; i++) {
            if (sortedIntervals[i].end > sortedIntervals[i+1].start) return false
        }

        return true
    }
}
