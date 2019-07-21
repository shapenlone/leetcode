
import java.util.HashMap;

public class Solution{
    public int[] twoSum(int[] nums,int target){
        HashMap<Integer,Integer> s = new HashMap<Integer,Integer>();
        int[] result = new int[2];
        for (int i = 0; i < nums.length; i++) {
            if(s.containsKey(target-nums[i])){
                result[1] = i;
                result[0] = s.get(target-nums[i]);
                return result;
            }
            s.put(nums[i],i);
        }
        return result;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] param = {1,3,5,7};
        int[] a = s.twoSum(param,8);
        System.out.printf("%d,%d",a[0],a[1]);
    }
}