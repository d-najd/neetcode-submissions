public class DynamicArray {
    private int[] _array;
    private int _size;
    private int _capacity;
    
    public DynamicArray(int capacity)
    {
        _array = new int[capacity];
        _size = 0;
        _capacity = capacity;
    }

    public int Get(int i)
    {
        return _array[i];
    }

    public void Set(int i, int n)
    {
        _array[i] = n;
        if (i > _size)
        {
            _size = i;
            _capacity = i;
        }
    }

    public void PushBack(int n)
    {
        if (_capacity == _size)
        {
            Resize();
        }

        _array[_size] = n;
        _size++;
    }

    public int PopBack()
    {
        _size--;
        var last = _array[_size];
        if (_capacity < _size)
        {
            var newArray = new int[_size];
            Array.Copy(_array, newArray, _size);
            _array = newArray;
        }

        return last;
    }

    private void Resize()
    {
        _capacity *= 2;
        var newArray = new int[_capacity];
        Array.Copy(_array, newArray, _size);
        _array = newArray;
    }

    public int GetSize()
    {
        return _size;
    }

    public int GetCapacity()
    {
        return _capacity;
    }
}
