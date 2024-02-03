package Leetcode_Problems;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class problem1 {
    public int[] twoSum(int[] nums, int target) {
      Map<Integer, Integer> numToIndex = new HashMap<>();
  
      for (int i = 0; i < nums.length; ++i) {
        if (numToIndex.containsKey(target - nums[i]))
          return new int[] {numToIndex.get(target - nums[i]), i};
        numToIndex.put(nums[i], i);
      }
  
      throw new IllegalArgumentException();
    }
  }