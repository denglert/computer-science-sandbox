# Sorting


**Sorting algorithms:**
- Quicksort ([wiki][quicksort_wiki])
- Merge sort ([wiki][mergesort_wiki])
- Heapsort ([wiki][heapsort_wiki])


**Occurances in practice:**
- https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.sort.html
- https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.argsort.html



## From `numpy` manuals

> The various sorting algorithms are characterized by their average speed, worst case performance,
> work space size, and whether they are stable. A stable sort keeps items with the same key in the
> same relative order. The three available algorithms have the following properties:

> | kind        | speed | worst case  | work space | stable |
> | ---------   | ----- | ----------  | ---------- | ------ |
> | quicksort   | 1     | O(n^2)      | 0          | no     |
> | ‘mergesort’ | 2     | O(n*log(n)) | ~n/2       | yes    |
> | ‘heapsort’  | 3     | O(n*log(n)) | 0          | no     |

[quicksort_wiki]: https://en.wikipedia.org/wiki/Quicksort
[mergesort_wiki]: https://en.wikipedia.org/wiki/Merge_sort
[heapsort_wiki]: https://en.wikipedia.org/wiki/Heapsort
