#include "quicksort.h"
#include <iostream>

int divideSortPivot(int arr[], int left, int right){
	int pivotUnsorted=((right-left)/2)+left;
	int pivot=arr[pivotUnsorted];
	int i=-1;

	for (int j = left; j <=right; ++j)
	{
		if(arr[j]<=pivot){
			++i;
		}
	}
	int pivotIndex=i+left;
	i=left-1;
	for(int j=left;j<=right;++j){
		if(arr[j]<=pivot){
			++i;
			if(j==pivotUnsorted){
				pivotUnsorted=i;
			}
			std::swap(arr[i],arr[j]);
		}
	}
	std::swap(arr[pivotIndex],arr[pivotUnsorted]);
	return (pivotIndex);
}

void quicksort(int arr[], int left, int right){
	if (left>=right)
	return;

	int pivot=divideSortPivot(arr,left,right);

	quicksort(arr,left,right);
	quicksort(arr,pivot+1,right);
}

void quicksort(int arr[], int arrLenght){
	quicksort(arr,0,arrLenght-1);
}