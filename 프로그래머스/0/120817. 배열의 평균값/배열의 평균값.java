class Solution {
    public double solution(int[] numbers) {
        double sum=0;
        for (int i = 0; i < numbers.length ; i++)
        {
            sum+=numbers[i];
         }
        System.out.print(numbers.length);
        return sum/numbers.length;
    }
}