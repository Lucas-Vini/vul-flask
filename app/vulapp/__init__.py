from app.vulapp.views.auth import auth
from app.vulapp.views.sql_injection	import sql_injection
from app.vulapp.views.cross_site_scripting import cross_site_scripting
from app.vulapp.views.profile import profile

__all__ = ["auth", "sql_injection", "cross_site_scripting", "profile"]