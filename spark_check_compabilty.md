<html>
<body>
<h1>Проверка совместимости версий Apache Spark 3.2.1 and 3.1.2</h1>
<i>Заниматься такой задачей не доводилось, но попробую :)</i><br><br>
<p>На оф сайте <a href="https://spark.apache.org">спарка</a> нашел описание апдейтов, которые нужны для задания 
<a href="https://spark.apache.org/releases/spark-release-3-1-2.html">3.1.2</a> и 
<a href="https://spark.apache.org/releases/spark-release-3-2-1.html">3.2.1</a></p>
<p>Возможные проблемы при переходе на новую версию:
<ul>
    <li>Deterministic flag is not handled for V2 functions (не очень понял, речь идет о какой-то конкретной функции или о спарке 2 версии)</li>
    <li>Python UDF after off-heap vectorized reader can cause crash due to use-after-free in writer thread</li>
    <li>Avoid fetching merge status when shuffleMergeEnabled is false for a shuffleDependency during retry</li>
    <li>Disable two level of map for final hash aggregation by default</li>
</ul>
</p>

<p>Возможные варианты решения проблем:
<ul>
    <li>
        Если речь про функцию, то соответственно не использовать детерминированные флаги в функции V2, переписать скрипты, использующие эту функцию
    </li>
    <li>
        Внимательно относиться к векторизированному чтению через питон, так как могут быть сбои (может быть изменить метод чтения с векторизированного на другой?)
    </li>
    <li>
        Смотреть за параметром настройки (сессии?) shuffleMergeEnabled, если его значение false (соответственно, может быть поможет параметр true, для избегания данной проблемы?)
    </li>
    <li>
        Отключать двухуровневую карту для агрегации хешей
    </li>
</ul>
</p>

<p>P.S. Как делал? Зашел на сайт спарка, почитал чейнджлоги этих двух версий, посмотрел какие могут быть предупреждения или ошибки в версии 3.2.1 и их решил вынести в маркированный список. Попытался осознать это и придумать какие-то простые решения этих проблем.</p>
</body>
</html>