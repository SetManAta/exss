from . import views
from . import app

# urls for posts
app.add_url_rule('/', view_func=views.index, methods=['GET'], endpoint='index')
app.add_url_rule('/employee/create', view_func=views.employee_create, methods=['GET', 'POST'], endpoint='employee_create')
app.add_url_rule('/employee/<int:id>', view_func=views.employee_detail, methods=['GET'], endpoint='employee_detail')
app.add_url_rule('/employee/<int:id>/delete', view_func=views.employee_delete, methods=['GET', 'POST'], endpoint='employee_delete')
app.add_url_rule('/employee/<int:id>/update', view_func=views.employee_update, methods=['GET', 'POST'], endpoint='employee_update')


# urls for user

app.add_url_rule('/register', view_func=views.register, methods=['GET', 'POST'], endpoint='register')
app.add_url_rule('/login', view_func=views.login, methods=['GET', 'POST'], endpoint='login')
app.add_url_rule('/logout', view_func=views.logout, methods=['GET'], endpoint='logout')
