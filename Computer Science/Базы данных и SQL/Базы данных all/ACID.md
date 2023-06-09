![[ACID-Properties.jpg]]
Транзакции это совокупность операций над данными.

Транзакция это одна единица работы бд, во время которой происходит доступ к данным и, возможно, их модификация.

Транзакции используют операции чтения и записи.
 
Для того чтобы поддерживать постояноство/непротиворечивость/однородность в БД перед и после транзакции должны быть соблюдены определённые свойства. 

Они называются свойствами ACID.

#### Atomicity - Атомарность.
 
Даже комплексная транзакция, состоящия из множества операций обращения к данным, представляет из себя единое целое, и должна или быть выполнена целиком или не выполнена совсем.

Это задействует две операции:
Отмену и коммит.

#### Consistency
Означает, что данные в хорошем состоянии.
Однородном, непротиворечивом.
Т.е. для них выполняется набор определённых правил:
например, что не может быть людей старше двухсот лет или не может быть сотни стран с одним названием.

Если перед транзакцией данные были консистентны, то и после они тоже должны быть консистентны.
Вот только поддержание этого это задача приложения, а не БД. 
БД сгодится только для простых правил.

#### Isolation
race condition 

[[уровни изоляции транзакций]]

Уровни изоляции:
1. Serializible. Т.е. последовательный доступ транзакций к бд (очередь)
2. Read committed
   dirty read это когда другие транзакции видят то, что изменила, но ещё не закоммитила другая транзакция. это read uncommitted
   чем плох read committed?
   простой пример- две транзакции.
   первая- получить число строк и получить и вывести все строки, вторая- добавляет новую строку.
   если вторая закончится между операциями первой, то выведется на одну строку больше, чем отображаемое число
3. snapshot isolation/repeatable read

Какие могут быть проблемы с любыми уровнями изоляции?
Lost update. Например, надо прочитать значение счётчика, прибавить единичку и записать обратно.
Обе транзакции считывают значение, и записывают одинаковые обратно.

Как решается? 
atomic updates, когда в одном запросе мы и читаем и обновляем, это эксклюзивная блокировка.
explicit lock - тоже самое, но вручную
lost update detection- автоматическая отмена 

#### Durability
После коммита изменения запишутся, на жёсткий диск, а не останутся в оперативке.

