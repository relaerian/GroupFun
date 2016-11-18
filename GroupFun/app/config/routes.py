from system.core.router import routes

routes['default_controller'] = 'Users'
routes['/users'] = 'Users#index'
routes['/users/new'] = 'Users#new'
routes['POST']['/users/create'] = 'Users#create'
routes['/users/show/<int:id>'] = 'Users#show'
routes['/users/edit/<int:id>'] = 'Users#edit'
routes['POST']['/users/update/<int:id>'] = 'Users#update'
routes['/users/delete/<int:id>'] = 'Users#delete'
routes['/users/destroy/<int:id>'] = 'Users#destroy'
