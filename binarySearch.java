class BinarySearch {
	public static int binarySearch(int a[],int low,int high,int key) {
	    if (low<=high) {
	    	int mid=(low+high)/2;
		    if(a[mid]==key) {
			      return mid;
		}
		else if(a[mid]<key) {
			return binarySearch(a,mid+1,high,key);
		}
		else {
			return binarySearch(a,low,mid-1,key);
	    }
				
	}
	return -1;
}
public static void main(String args[]) {
	int a[]= {1,3,5,7,9,11,23,55};
	int low=0;
	int high=a.length-1;
	int key=7;
	int result=binarySearch(a,0,high,key);
	if (result==-1) {
		System.out.print("not found");
	}
	else {
		System.out.print("found at:"+result);
			
	}
			
}
}

