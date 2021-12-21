import java.util.*;

public class Main {

	public static void main(String[] args) {
		System.out.println(binarySearch(new int[] {-1,0,1,2,3,4},3));
	}
	
	/*
	 * Takes a sorted arr and a val
	 * and returns the smallest index i such that val<=arr[i]
	 * */
	
	public static int binarySearch(int[] arr,int val) {
		int left=-1;
		int right=arr.length;
		
		//INV: (left==-1 || arr[left]<val) && (right==arr.length || val<=arr[right])
		
		while(right-left>1) {
			int mid=(left+right)/2;
			if(arr[mid]<val)
				left=mid;
			else
				right=mid;
		}
		return right;
		
	}
	
	static int pre;
	static int post;
	
	/*
	 * Takes directed graph g in adjacency list format.
	 * Where g[u].contains(v) <=> (u,v) \in E
	 * and prints the pre and post number of the dfs traversal
	 * */
	
	public static void dfs(List<Integer>[] g,int start) {
		pre=1;
		post=1;
		recdfs(g,new boolean[g.length],start);
	}
	
	public static void recdfs(List<Integer>[] g,boolean[] visited,int u) {
		visited[u]=true;
		for(int v:g[u]) {
			if(!visited[v]) {
				//pre
				System.out.println("Node "+v+" has prenumber "+(pre++));
				recdfs(g,visited,v);
				//post
				System.out.println("Node "+v+" has postnumber "+(post++));
			}
		}
		
	}
	
	/*
	 * Takes directed graph g in adjacency list format,
	 * Where g[u].contains(v) <=> (u,v) \in E, and a start node
	 * and returns the distance from start using bfs
	 * */
	
	public static int[] bfs(List<Integer>[] g,int start) {
		int[] dist = new int[g.length];
		for (int i = 0; i < dist.length; i++) {
			dist[i]=Integer.MAX_VALUE;
		}
		
		LinkedList<Integer> queue = new LinkedList<Integer>();
		dist[start]=0;
		queue.addFirst(start);
		while(!queue.isEmpty()) {
			int u=queue.removeLast();
			for(int v: g[u]) {
				if(dist[v]==Integer.MAX_VALUE) {
					dist[v]=dist[u]+1;
					queue.addFirst(v);
				}
			}
		}
		
		return dist;
	}
	
	/*
	 * Takes directed weighted graph g in adjacency list format,
	 * Where g[u] is the list which contains for every edge (u,v) with w((u,v))=z an Edge object with to=v and weight=z
	 * and returns the distance from start using dijkstra algorithm
	 * */
	
	public static int[] dijkstra(List<Edge>[] g,int start) {
		int[] dist = new int[g.length];
		for (int i = 0; i < dist.length; i++) {
			dist[i]=Integer.MAX_VALUE;
		}
		
		PriorityQueue<Node> q = new PriorityQueue<Node>();
		q.add(new Node(start,0));
		while(!q.isEmpty()) {
			Node cur=q.poll();
			if(cur.w<dist[cur.u]) {
				dist[cur.u]=cur.w;
				for(Edge e:g[cur.u]) {
					q.add(new Node(e.to,cur.w+e.weight));
				}
			}
		}
		
		return dist;
	}

}

class Edge{
	int to,weight;
	Edge(int to,int weight){
		this.to=to;
		this.weight=weight;
	}
}

class Node implements Comparable<Node>{
	int u,w;
	
	Node(int u,int w){
		this.u=u;
		this.w=w;
	}
	@Override
	public int compareTo(Node o) {
		return w-o.w;
	}
	@Override
	public String toString() {
		return u+" "+w;
	}
}
