# 1 \_\_dict\_\_
* атрибут, автоматично генериран за всеки клас получава
* речник
* съдържа symbol table
* съдържа всички полета (пропъртита, дейта атрибути)
  на инстанцията
# 2 getattr, setattr, delattr, hasattr
* вградени функции
* 1во предимство на getattr спрямо точката "." е че може да се 
получи стойността динамично
* удобно е когато не знаем предварително имената на атрибутите,
а ще ги получим като стринг в последствие
* 2ро предимство: може като 3-ти аргумент да дадем стойност по
подразбиране (ако няма поле, пропърти, дейта атрибут с такова име)
  
# 3.1 Static методи

* просто казано, нямат достъп до self
* Нещо подобно на клас атрибутите, общи са за всички инстанции
* методи, в които нямаме достъп до стейт на обекта (състояние)
* Utility методи
* използваме статик методи когато не ползваме селф в тялото на
метода; това е добрата практика
* съвсем спокойно може и да е изнесен извън класа
* слагаме го вътре защото е свързан логически с класа; класът
  ги дообеснява
* @ е декоратор; Накратко, декоратор е ф-я която се изпълнява
преди нашата фунцкия
* декораторите променят начина по който работят фунциите

# 3.2 Клас методи
* получават класа като параметър
* при питон, в клас не може да имаме няколко фунцкии 
  с едно и също име (така наречено function overloading)
* метод, който създава обекти типично е класс метод; нарича се
  метод-фабрика, factory method
* при наследяване, клас методите се наследяват, статик 
  методите - не се
  