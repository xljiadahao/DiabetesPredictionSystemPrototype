from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'neuralnetwork.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'neuralnetwork.controller.home'),
    url(r'^main/$', 'neuralnetwork.controller.main'),
    url(r'^dataProcessing/$', 'neuralnetwork.controller.dataProcessing'),
    url(r'^showRawData/$', 'neuralnetwork.controller.showRawData'),
    url(r'^process/$', 'neuralnetwork.controller.process'),
    url(r'^showDataProcessed/$', 'neuralnetwork.controller.showDataProcessed'),
    url(r'^trainingAndTest/$', 'neuralnetwork.controller.trainingAndTest'),
    url(r'^testResult/$', 'neuralnetwork.controller.testResult'), 
    url(r'^prediction/$', 'neuralnetwork.controller.prediction'),
    url(r'^predictionMultiple/$', 'neuralnetwork.controller.predictionMultiple'),
    url(r'^uploadFileAndPredict/$', 'neuralnetwork.controller.uploadFileAndPredict'),
    url(r'^predictionSingle/$', 'neuralnetwork.controller.predictionSingle'),
    url(r'^predictionSingleResult/$', 'neuralnetwork.controller.predictionSingleResult'),
    url(r'^admin/', include(admin.site.urls)),
)
