public class DynamicArray {
    private int[] _arr { get; set; }
    public int Size { get; private set; }
    public int Capacity { get; private set; }
    public DynamicArray(int Capacity) {
        this.Capacity = Capacity;
        _arr = new int[Capacity];
        Size = 0;
    }

    public int Get(int i) {
        if (!InBounds(i)) {
            return -1;
        }
        return _arr[i];
    }

    private bool InBounds(int i) {
        return (0 <= i && i < Size);
    }

    public void Set(int i, int n) {
        if (InBounds(i)) {
            _arr[i] = n;
        }
    }

    public void PushBack(int n) {
        if (Size == Capacity) {
            Resize();
        }
        _arr[Size] = n;
        Size++;
    }

    public int PopBack() {
        int Temp = _arr[Size-1];
        _arr[Size-1] = 0;
        Size--;
        return Temp;
    }

    private void Resize() {
        Capacity *= 2;
        int[] Temp = new int[Capacity];
        Console.WriteLine(Capacity);
        for (int i = 0; i < Size; i++) {
            Temp[i] = _arr[i];
        }
        _arr = Temp;
    }

    public int GetSize() {
        return Size;
    }

    public int GetCapacity() {
        return Capacity;
    }
}
