import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

class Scratch {
    public static void main(String[] args) {
        var myHeap = new GenericHeap<Integer>((x, y) -> x - y);
        myHeap.insert(10);
        myHeap.insert(14);
        myHeap.insert(27);
        myHeap.insert(9);
        myHeap.insert(19);
        myHeap.insert(27);
        myHeap.insert(1);

        System.out.println("Heap with data: ");
        System.out.println(myHeap);

        ArrayList<Integer> sortedList = new ArrayList<>();

        while (myHeap.getSize() > 0) {
            sortedList.add(myHeap.delete());
        }

        System.out.println("\nSorted Array List made from popping off of heap: ");
        System.out.println(sortedList.toString());
    }
}

class GenericHeap<T> {

    private ArrayList<T> storage = new ArrayList<>();
    private Comparator<T> comparator;

    public GenericHeap(Comparator<T> comparator) {
        this.comparator = comparator;
    }

    public void insert(T value) {
        storage.add(value);
        bubbleUp(storage.size() - 1);
    }

    public T delete() {
        Collections.swap(storage, 0, storage.size() - 1);
        T value = storage.remove(storage.size() - 1);
        siftDown(0);

        return value;
    }

    public T getPriority() {
        return storage.get(0);
    }

    public int getSize() {
        return storage.size();
    }

    private void bubbleUp(int index) {
        /*
         * takes the object at index (child) and uses comparator to check if child has
         * priority over parent, if child does method swaps child with parent and
         * continues checking against next parent until no more swaps occur
         */
        while (index > 0) {
            // get parent of item at index using
            int parent = (index - 1) / 2;

            T parentValue = storage.get(parent);
            T indexValue = storage.get(index);

            if (comparator.compare(parentValue, indexValue) > 0) {
                // if child has priority swap with parent and update
                // index to reflect out new position
                Collections.swap(storage, index, parent);
                index = parent;
            } else {
                break;
            }

        }

    }

    private void siftDown(int index) {
        /*
         * Takes the element in storage at index and checks to see that it has priority
         * over children. if element does not have priority swaps the element with child
         * and updates index to be the elements new location Then continues to do this
         * until there are no more swaps made
         */

        while (index < storage.size()) {
            // get value of item at index we are sifting from
            T index_val = storage.get(index);

            // get indexes of left and right child
            int left = index * 2 + 1;
            int right = index * 2 + 2;

            // if item at index has a left and right child
            if (left < storage.size() && right < storage.size()) {
                T left_val = storage.get(left);
                T right_val = storage.get(right);

                // if right child has priority over right child
                if (comparator.compare(left_val, right_val) > 0) {
                    // if right child has priority over parent
                    if (comparator.compare(index_val, right_val) > 0) {
                        Collections.swap(storage, right, index);
                        index = right;
                    } else {
                        // if it doesnt no need to keep comparing
                        break;
                    }

                    // if left child has priority over right
                } else {
                    // if left child has priority over parent
                    if (comparator.compare(index_val, left_val) > 0) {
                        Collections.swap(storage, left, index);
                        index = left;
                    } else {
                        break;
                    }
                }
                // if there is only a left item
            } else if (left < storage.size()) {
                T left_val = storage.get(left);

                if (comparator.compare(index_val, left_val) > 0) {
                    Collections.swap(storage, left, index);
                    index = left;
                } else {
                    break;
                }

                // if neither of those are the case
            } else {
                break;
            }
        }
    }

    @Override
    public String toString() {
        return storage.toString();
    }
}