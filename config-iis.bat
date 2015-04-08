SET PYTHON_HOME=C:\Anaconda
SET SITE_ROOT=%cd%
SET PROJECT_NAME=Web

start /wait %windir%\System32\PkgMgr.exe /iu:IIS-WebServerRole;IIS-WebServer;IIS-CommonHttpFeatures;IIS-StaticContent;IIS-DefaultDocument;IIS-DirectoryBrowsing;IIS-HttpErrors;IIS-HealthAndDiagnostics;IIS-HttpLogging;IIS-LoggingLibraries;IIS-RequestMonitor;IIS-Security;IIS-RequestFiltering;IIS-HttpCompressionStatic;IIS-WebServerManagementTools;IIS-ManagementConsole;WAS-WindowsActivationService;WAS-ProcessModel;WAS-NetFxEnvironment;WAS-ConfigurationAPI;IIS-CGI


%windir%\system32\inetsrv\appcmd set config /section:system.webServer/fastCGI "/+[fullPath='%PYTHON_HOME%\python.exe', arguments='%PYTHON_HOME%\Scripts\wfastcgi.py']"


%windir%\system32\inetsrv\appcmd set config /section:system.webServer/handlers "/+[name='Python_via_FastCGI',path='*',verb='*',modules='FastCgiModule',scriptProcessor='%PYTHON_HOME%\python.exe|%PYTHON_HOME%\Scripts\wfastcgi.py',resourceType='Unspecified']"


%windir%\system32\inetsrv\appcmd set config -section:system.webServer/fastCgi /+"[fullPath='%PYTHON_HOME%\python.exe', arguments='%PYTHON_HOME%\Scripts\wfastcgi.py'].environmentVariables.[name='WSGI_HANDLER',value='django.core.handlers.wsgi.WSGIHandler()']" /commit:apphost


%windir%\system32\inetsrv\appcmd set config -section:system.webServer/fastCgi /+"[fullPath='%PYTHON_HOME%\python.exe', arguments='%PYTHON_HOME%\Scripts\wfastcgi.py'].environmentVariables.[name='DJANGO_SETTINGS_MODULE',value='%PROJECT_NAME%.settings']" /commit:apphost


%windir%\system32\inetsrv\appcmd set config -section:system.webServer/fastCgi /+"[fullPath='%PYTHON_HOME%\python.exe', arguments='%PYTHON_HOME%\Scripts\wfastcgi.py'].environmentVariables.[name='PYTHONPATH',value='%SITE_ROOT%']" /commit:apphost

