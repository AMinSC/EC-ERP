from django.contrib import admin
from .models import (UserProfile
                    , Authority
                    , AuthorityMenu
                    , InstallationRequest
                    , Dealer
                    , Client
                    , ASRegister
                    , History
                    , Contractor
                    , Combo)


admin.site.register(UserProfile)
admin.site.register(Authority)
admin.site.register(AuthorityMenu)
admin.site.register(InstallationRequest)
admin.site.register(Dealer)
admin.site.register(Client)
admin.site.register(ASRegister)
admin.site.register(History)
admin.site.register(Contractor)
admin.site.register(Combo)
