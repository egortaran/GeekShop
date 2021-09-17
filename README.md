# Интернет магазин
Apps: ```adminapp```, ```authapp```, ```basketapp```, ```mainapp```, ```ordersapp```
<p align="center">
  <img src="https://github.com/egortaran/GeekShop/blob/main/image/main.png">
</p>

В данном интернет магазине реализовано:
  - Аутентификация  и регистрация пользователя. Регистрация пользователя через социальную сеть ВКонтакте
  - Отправка электронной почты, подтверждение email пользвателя
  - Добавление товара в корзину. Редактирование количества товара в корзине
  - Собственная админка. Заказ/Категория/Товар/Пользователи
  - Кеширование

## Вход в систему
### Авторизация
Для того, чтобы авторизоваться, нужно нажать на **"войти"**. Вы можете зайти в систему в качестве администратора с логином *"django"* и пароль *"123"*, или **зарегистироваться**, а также выполнить **"Вход через ВКонтакте"**.

<p align="center">
  <img src="https://github.com/egortaran/GeekShop/blob/main/image/login.png">
</p>

### Регистрация
При регистрации нужно заполнить поля снизу. Для подтверждения пользователя требуется подтвердить email.
<p align="center">
  <img src="https://github.com/egortaran/GeekShop/blob/main/image/register.png" height="700">
</p>

## Товар
После регистрации мы можем выбрать товар и добавить его в корзину. Для этого достаточно на "Главной" в разделе "Популярные" нажать на интересующий нас товар, либо перейти во вкладку "Продукты".

### Продукты
При переходе в "Продукты" отображается товар с надписью **горячее предложение**. Следом идет идентичный блок "Популярные" и блок "Похожие продукты". В примере **горячее предложение** - "Ваза" из категории "Другое".
<table>
  <tr>
    <td>
      <p align="center">Горячее предложение</p>
    </td>
    <td>
      <p align="center">Похожие продукты</p>
    </td>
  </tr>
  <tr>
    <td><img src="https://github.com/egortaran/GeekShop/blob/main/image/hot_product.png" alt=""  width="600" height="400"></td>
     <td><img src="https://github.com/egortaran/GeekShop/blob/main/image/look.png" alt="" width="460" height="240"></td>
  </tr>
</table>

  - Горячее предложение формируется случайным выбором **Product** из базы данных с помощью функции ```get_hot_product()```.
  - Похожие продукты выбираются идентичной категории **Product** с помощью функции ```get_same_products()```

### Категория товара
Пользователь может перейти ко всем, или к трём следующим категорям: "Стулья", "Лампы", "Другое". При переходе к категории, отбражается случайный товар. В "Популярные" отображаются два случайных товара этой же категории, а в "Похожие продукты" все товары выбранной категории.

### Пагинатор
С помощью пагинатора возможно переключение между товарами категории. Ниже представлена работа пагинатора категории "Стулья". 

<table>
  <tr>
    <td><img src="https://github.com/egortaran/GeekShop/blob/main/image/pg_1.png" alt=""  width="640" height="341"></td>
    <td><img src="https://github.com/egortaran/GeekShop/blob/main/image/pg_2.png" alt="" width="640" height="341"> </tr>
</table>

### Весь список товаров
<p align="center">
  <img src="https://github.com/egortaran/GeekShop/blob/main/image/all_product.png">
</p>

## Корзина
### Добавление товара в корзину
Добавить товар можно, нажав на **Заказать**. В качестве примера взята "Настольная лампа" из категории "Лампы". В меню страницы появится корзина с суммой заказа и количеством товара в ней.
<p align="center">
  <img src="https://github.com/egortaran/GeekShop/blob/main/image/basket_order.png">
</p>
Добавим еще "Часы" из категории "Другое", после чего перейдем в козину. В корзине можно изменить количество товара, общая стоимость обновиться автоматически. Одним кликом можно удалить товар из корзины.

<p align="center">
  <img src="https://github.com/egortaran/GeekShop/blob/main/image/basket.png">
</p>

## Админка
Для перехода в Админ. панель досточно нажать на **пользователь**, после чего можно выбрать:
  - Менеджер. Кастомизированная админка
  - Админка. Django
  - А так же можно посмотреть свою информацию и изменить ее.
<p align="center">
  <img src="https://github.com/egortaran/Prepare_readme/blob/main/image/%D0%BF%D1%80%D0%BE%D1%84_%D0%BC%D0%B5%D0%B4_%D0%B0%D0%B4%D0%BC.png">
</p>

## Админка Django
На сайте можно использовать админку от Django. **Пользователи**, **Корзина**, **Категории**, **Товары**, **Заказы** доступны к редактированию.
<p align="center">
  <img src="https://github.com/egortaran/Prepare_readme/blob/main/image/%D0%B0%D0%B4%D0%BC_django.png">
</p>

## Кастомизированная админка
### Категории
Для начала рассмотрим **Категории**. Доступно:
  - Товары категории
  - Редактировать
  - Удалить
<p align="center">
  <img src="https://github.com/egortaran/Prepare_readme/blob/main/image/%D0%BA%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D0%B8.png">
</p>

#### Товары категории
Их также можно **посмотреть**, **редактировать** и **удалить/востановить** (используется параметр ```is_active```).
<p align="center">
  <img src="https://github.com/egortaran/Prepare_readme/blob/main/image/%D0%A2%D0%BE%D0%B2%D0%B0%D1%80%D1%8B%20%D0%BA%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D0%B8.png">
</p>

#### Редактировать
При добавленни скидки изменяется цена на все товары данной категории. **Имя** категории, **Описание**, ```is_active``` доступны к редактированию.
<p align="center">
  <img src="https://github.com/egortaran/Prepare_readme/blob/main/image/%D1%80%D0%B5%D0%B4%D0%B0%D0%BA%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5.png">
</p>

### Заказ
#### Добавление заказа
Заказ формируется от корзины пользователя. При создании заказа мы также можем его отредактировать. Нажав на **сохранить**, мы создаем заказ, который требуется подтвердить.
<p align="center">
  <img src="https://github.com/egortaran/Prepare_readme/blob/main/image/%D0%97%D0%B0%D0%BA%D0%B0%D0%B7_%D0%BD%D0%BE%D0%B2%D1%8B%D0%B9.png">
</p>

#### Подтверждение заказа
Отображается информация о заказе. Нажав на **совершить покупку**, идет подтверждение. Обновление происходит при помощью ```models.DateTimeField(auto_now=True)```
<p align="center">
  <img src="https://github.com/egortaran/Prepare_readme/blob/main/image/%D0%9F%D0%BE%D0%B4%D1%82%D0%B2%D0%B5%D1%80%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B7%D0%B0%D0%BA%D0%B0%D0%B7%D0%B0.png">
</p>

#### Просмотр заказов
И, наконец, просмотр всех заказов. **CRUD** операции доступны на этой странице
<p align="center">
  <img src="https://github.com/egortaran/Prepare_readme/blob/main/image/%D0%B2%D1%81%D0%B5%20%D0%B7%D0%B0%D0%BA%D0%B0%D0%B7%D1%8B.png">
</p>
