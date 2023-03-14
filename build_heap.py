# python3


def build_heap(data):
    swaps = []
    sz = len(data)   
    
    def heapify(i):
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        
        if left < sz and data[left] < data[smallest]:
            smallest = left
            
        if right < sz and data[right] < data[smallest]:
            smallest = right
            
        if smallest != i:
            swaps.append([i, smallest])
            data[i], data[smallest] = data[smallest], data[i]
            heapify(smallest)

    for i in range(int(sz / 2), -1, -1):
        heapify(i)
        
    return swaps


def main():
    input_type = input()

    if "F" in input_type:
        filename = input()
        if ".a" in filename:
            return
        if "test/" not in filename:
            filename = "test/" + filename
        if "test/" in filename:    
            with open(filename) as f:
                n = int(f.readline().strip())
                data = list(map(int, f.readline().strip().split()))
                swaps = build_heap(data)

    elif "I" in input_type:
        n = int(input())
        data = list(map(int, input().split()))
        swaps = build_heap(data)

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
