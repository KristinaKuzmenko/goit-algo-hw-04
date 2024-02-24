
## Порвняльна таблиця швидкості алгоритмів сортування для різних даних
| Algorithm            | Small                | Medium               | Large                |
| -------------------- | -------------------- | -------------------- | -------------------- |
| Insertion Sort       |              0.00548 |              0.48540 |             54.69662 |
| Merge Sort           |              0.00300 |              0.04327 |              0.58543 |
| Quicksort            |              0.00219 |              0.02728 |              0.25267 |
| Bubble Sort          |              0.00909 |              1.08550 |            121.10756 |
| Timsorted            |              0.00011 |              0.00147 |              0.02639 |
| Timsort              |              0.00009 |              0.00130 |              0.02629 |


## Висновки
Було заміряно час виконання алгоритмів сортування вставками Insertion Sort, злиттям Merge Sort, швидкого сортування Quicksort, сортування бульбашкою Bubble Sort та вбудованих у Python функції sorted() і методу sort() на масивах цілих чисел із 100, 1000, 10000 елементів.
- Найбільший час виконання в алгоритму сортування бульвашкою як на менших, так в на більших обсягах даних. При цьму, чим більше обсяг даних, тим більше рвзниця в часі виконання сортування бульбашкою та, наприклад, швидким сортуванням. Це відбувається, оскільки часова складність сортування бульбашкою O(n^2), тому зі збільшенням обсягу даних час виконання дуже швидко зростає. Схожа ситуація із алгоритмом сортування вставками, хоча емпірично він працює приблизно в 2 рази швидше, ніж сортування бульбашкою. 
- Сортування злиттям працює значно швидше, зі збільшенням обсягу даних час його виконання зростає не так швидко, оскільки чова складність цього алгоритму ``O(n*logn)``. Цікаво, що швидке сортування працює ще швидше при часовій складності ``O(n**2)`` у гіршому випадку та ``O(n*logn)`` у середньому випадку. Оскільки ми виконали цей алгоритм 30 разів, його часова складність близька до часової складності середнього випадку. В той же час, алгоритм сортування злиттям використовує додатковий обсяг пам'яті, що може впливати і на час виконання. 
- Найшвидшими алгоритмами сортування виявились вбудовані в Python функція sorted() і метод sort(). Вони використовують алгоритм Timsort, що є комбінацією алгоритму сортування вставками та сортування злиттям. Цей алгоритм має часову складність  O(n) в кращому випадку та ``O(n*logn)`` у середньму та гіршому випадку, емпірично на масивах цілих чисел алгортм працює на порядок швидше алгоритму Quick Sort. При цьому трохи швидше на малих і середніх даних працює метод sort(), який змінює вхідний масив, ніж функція sorted(), що повертає відсортовану копію. На великих даних різниці в часі виконання цих двох функцій майже немає.
- Отже, поєднання та оптимізація алгоритмів сортування вставками та злиттям в єдиний алгоритм сортування Timsort в рази підвищує швидкість сортування. Тому за наявності дуже ефективного вбудованого алгоритму немає необхідності писати свій.
