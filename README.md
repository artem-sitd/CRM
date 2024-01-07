`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py create_groups` 

Последняя команда создаст:

1. Администратора (staff) (crm_admin1),
2. оператора (operator),
3. менеджера (manager),
4. маркетолога (marketer). У всех пароли: `123`
5. Добавит их в группы: `'Operators', 'Marketers', 'Managers'