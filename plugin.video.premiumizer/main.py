# -*- coding: utf-8 -*-

from urlparse import parse_qsl
import sys
params = dict(parse_qsl(sys.argv[2].replace('?','')))

action = params.get('action')

icon = params.get('icon')

id = params.get('id')

type = params.get('type')

name = params.get('name')

title = params.get('title')

year = params.get('year')

imdb = params.get('imdb')

tvdb = params.get('tvdb')

tmdb = params.get('tmdb')

season = params.get('season')

episode = params.get('episode')

tvshowtitle = params.get('tvshowtitle')

premiered = params.get('premiered')

url = params.get('url')

image = params.get('image')

meta = params.get('meta')

select = params.get('select')

query = params.get('query')

source = params.get('source')

content = params.get('content')

if action == None:
    from resources.lib.indexers import navigator
    navigator.navigator().root()
	
elif action == 'play':
	from resources.lib.sources import sources	
	sources().play(title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, meta, select=select)
	
elif action == 'directPlay':
	from resources.lib.sources import sources	
	sources().directPlay(url, title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, meta, id)

elif action == 'authRealDebrid':
	from resources.lib.modules import control	
	from tvresolver import debrid	
	token = debrid.authRealDebrid()
	if token != '' and token != '0' and token != None:
		status = 'Tv Resolver Authorized'
		control.setSetting(id='realdebrid.status', value=status)
		control.openSettings('3.1')	
	
elif action == 'testItem':
	from resources.lib.api import fanarttv
	imdb = '121361'
	query = 'tv'
	fanarttv.get(imdb, query)	
elif action == 'testSources':
	from resources.lib.sources import sources	
	sources().advtestmode()	
	
elif action == 'nextaired':
	from resources.lib.api import tvdbapi
	tvdbapi.airingtoday().get()
	
elif action == 'helpNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().help()

elif action == 'changelogNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().changelog()
	
	
	
# PREMIUMIZE SECTION #################
elif action == 'premiumizeNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().premiumizeNav()
	
elif action == 'premiumizeAdd':
    from resources.lib.api import premiumize
    premiumize.add()
	
elif action == 'premiumizeAdd':
    from resources.lib.api import premiumize
    premiumize.add()

elif action == 'premiumizeTransfers':
    from resources.lib.api import premiumize
    premiumize.transferList()	

elif action == 'premiumizeClearFinished':
    from resources.lib.api import premiumize
    premiumize.clearfinished()	

elif action == 'premiumizerootFolder':
    from resources.lib.api import premiumize
    premiumize.getFolder('root')	

elif action == 'premiumizeOpenFolder':
    from resources.lib.api import premiumize
	
    premiumize.getFolder(id, meta=meta)	
	
elif action == 'premiumizeDeleteItem':
    from resources.lib.api import premiumize
    premiumize.deleteItem(id, type)	

elif action == 'downloadFolder':
    from resources.lib.api import premiumize
    premiumize.downloadFolder(name, id)	
	
elif action == 'premiumizeRename':
    from resources.lib.api import premiumize
    premiumize.renameItem(title, id, type)	

elif action == 'getSearchMovie':
    from resources.lib.indexers import movies
    movies.movies().getSearch(create_directory=True)

elif action == 'addToLibrary':
	from resources.lib.api import premiumize
	premiumize.addtolibrary_service(id=id, type=type, name=name)
	

elif action == 'forcecloudsync':
	from resources.lib.modules import updater
	updater.updatelibrary()	
	
elif action == 'service':
	from resources.lib.modules import control
	if control.setting('cachecloud.startup') == 'true':
		from resources.lib.api import premiumize
		premiumize.cloudCache(mode='new')
	from resources.lib.modules import updater
	updater.updatelibrary()		
		
elif action == 'clearPremiumize':
    from resources.lib.resolvers import debrid
    debrid.PremiumizeClear()
	
elif action == 'play_library':	
	print ("PREMIUMIZE LIBRARY", name, id)
	from resources.lib.api import premiumize
	premiumize.library_play().play(name, id)

elif action == 'selectivelibrary_nav':	
	from resources.lib.api import premiumize
	premiumize.selectivelibrary_nav()

elif action == 'selectiveLibraryManager':	
	from resources.lib.api import premiumize
	premiumize.selectiveLibraryManager(id, name)
	
	

elif action == 'premiumizeLibrary':
	import shutil, os, time, xbmc
	from resources.lib.modules import control
	from resources.lib.api import premiumize
	yes = control.yesnoDialog('This will Create Strm Files based on your Cloud Folder' ,'Are you sure you want to continue?', '')
	#print ("PREMIUMIZE SELECTION", yes)
	if yes == 1: 
		try:
			libraryPath = xbmc.translatePath(control.setting('library.path'))
			if control.setting('library.deleteold') != 'true': raise Exception()
			try: shutil.rmtree(libraryPath)
			except:pass
			for root, dirs, files in os.walk(libraryPath , topdown=True):
				dirs[:] = [d for d in dirs]
				for name in files:
					try:
						os.remove(os.path.join(root,name))
						os.rmdir(os.path.join(root,name))
					except: pass
							
				for name in dirs:
					try: os.rmdir(os.path.join(root,name)); os.rmdir(root)
					except: pass
			time.sleep(3)
		except: pass
	
	
		premiumize.library_service()	
	
	
elif action == 'tvdbFav':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().getTvdbFav()
	
elif action == 'tvdbAdd':
    from resources.lib.api import tvdbapi
    tvdbapi.addTvShow(tvshowtitle, tvdb)
	
elif action == 'tvdbRemove':
    from resources.lib.api import tvdbapi
    tvdbapi.removeTvShow(tvdb)
	
elif action == 'AuthorizeTvdb':
    from resources.lib.api import tvdbapi
    tvdbapi.forceToken()	
	
elif action == 'updateAddon':
    from resources.lib.modules import updater
    updater.update_addon()

elif action == 'updateSources':
    from resources.lib.modules import updater
    updater.update_sources()	
	
elif action == 'firstSetup':
    from resources.lib.modules import setupTools
    setupTools.FirstStart()	
	

	
elif action == 'movieFavourites':
    from resources.lib.indexers import movies
    movies.movies().favourites()
	
elif action == 'remoteManager':
    from resources.lib.api import remotedb
    if content == 'movie': remotedb.manager(imdb, tmdb, meta, content)
    else: remotedb.manager(imdb, tvdb, meta, content)
	
elif action == 'remotelibrary_movies':
    from resources.lib.api import remotedb
    remotedb.getMovies()
	
elif action == 'remotelibrary_tv':
    from resources.lib.api import remotedb
    remotedb.getTV()
	
elif action == 'tvFavourites':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().favourites()
	
elif action == 'addFavourite':
    from resources.lib.modules import favourites
    favourites.addFavourite(meta, content)

elif action == 'deleteFavourite':
    from resources.lib.modules import favourites
    favourites.deleteFavourite(meta, content)
	
elif action == 'moviesInProgress':
    from resources.lib.indexers import movies
    movies.movies().inProgress()	
	
elif action == 'tvInProgress':
    from resources.lib.indexers import episodes
    episodes.episodes().inProgress()

elif action == 'deleteProgress':
    from resources.lib.modules import favourites
    favourites.deleteProgress(meta, content)	
	
elif action == 'movieNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().movies()

elif action == 'movieliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().movies(lite=True)

elif action == 'mymovieNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mymovies()

elif action == 'mymovieliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mymovies(lite=True)

elif action == 'tvNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().tvshows()

elif action == 'tvliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().tvshows(lite=True)

elif action == 'mytvNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mytvshows()

elif action == 'mytvliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mytvshows(lite=True)

elif action == 'downloadNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().downloads()

elif action == 'libraryNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().library()
	


elif action == 'toolNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().tools()

elif action == 'searchNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().search()

elif action == 'viewsNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().views()

elif action == 'clearCache':
    from resources.lib.modules import control	
    from resources.lib.modules import cache
    cache.cache_clear()
    control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')

elif action == 'infoCheck':
    from resources.lib.indexers import navigator
    navigator.navigator().infoCheck('')

elif action == 'movies':
    from resources.lib.indexers import movies
    movies.movies().get(url)

elif action == 'moviePage':
    from resources.lib.indexers import movies
    movies.movies().get(url)

elif action == 'movieWidget':
    from resources.lib.indexers import movies
    movies.movies().widget()

elif action == 'movieSearch':
    from resources.lib.indexers import movies
    movies.movies().search()

elif action == 'moviePerson':
    from resources.lib.indexers import movies
    movies.movies().person()

elif action == 'movieGenres':
    from resources.lib.indexers import movies
    movies.movies().genres()

elif action == 'movieLanguages':
    from resources.lib.indexers import movies
    movies.movies().languages()

elif action == 'movieCertificates':
    from resources.lib.indexers import movies
    movies.movies().certifications()

elif action == 'movieYears':
    from resources.lib.indexers import movies
    movies.movies().years()

elif action == 'moviePersons':
    from resources.lib.indexers import movies
    movies.movies().persons(url)

elif action == 'movieUserlists':
    from resources.lib.indexers import movies
    movies.movies().userlists()

elif action == 'channels':
    from resources.lib.indexers import channels
    channels.channels().get()

elif action == 'tvshows':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().get(url)
	
elif action == 'tvshowsTvdb':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().getTvdb(url)
	

elif action == 'tvshowPage':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().get(url)

elif action == 'tvSearch':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().search()
	
elif action == 'tvSearchTvdb':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().searchTvdb()

elif action == 'tvPerson':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().person()

elif action == 'tvGenres':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().genres()

elif action == 'tvNetworks':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().networks()

elif action == 'tvLanguages':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().languages()

elif action == 'tvCertificates':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().certifications()

elif action == 'tvPersons':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().persons(url)

elif action == 'tvUserlists':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().userlists()

elif action == 'seasons':
    from resources.lib.indexers import episodes
    episodes.seasons().get(tvshowtitle, year, imdb, tvdb)

elif action == 'episodes':
    from resources.lib.indexers import episodes
    episodes.episodes().get(tvshowtitle, year, imdb, tvdb, season, episode)

elif action == 'calendar':
    from resources.lib.indexers import episodes
    episodes.episodes().calendar(url)

elif action == 'tvWidget':
    from resources.lib.indexers import episodes
    episodes.episodes().widget()

elif action == 'calendars':
    from resources.lib.indexers import episodes
    episodes.episodes().calendars()

elif action == 'episodeUserlists':
    from resources.lib.indexers import episodes
    episodes.episodes().userlists()

elif action == 'refresh':
    from resources.lib.modules import control
    control.refresh()

elif action == 'queueItem':
    from resources.lib.modules import control
    control.queueItem()

elif action == 'openSettings':
    from resources.lib.modules import control
    control.openSettings(query)

elif action == 'artwork':
    from resources.lib.modules import control
    control.artwork()

elif action == 'addView':
    from resources.lib.modules import views
    views.addView(content)

elif action == 'moviePlaycount':
    from resources.lib.modules import playcount
    playcount.movies(imdb, query)

elif action == 'episodePlaycount':
    from resources.lib.modules import playcount
    playcount.episodes(imdb, tvdb, season, episode, query)

elif action == 'tvPlaycount':
    from resources.lib.modules import playcount
    playcount.tvshows(name, imdb, tvdb, season, query)

elif action == 'trailer':
    from resources.lib.modules import trailer
    trailer.trailer().play(name, url)

elif action == 'traktManager':
    from resources.lib.api import trakt
    trakt.manager(name, imdb, tvdb, content)

elif action == 'authTrakt':
    from resources.lib.api import trakt
    trakt.authTrakt()

elif action == 'download':
    from resources.lib.api import premiumize
    premiumize.downloadItem(name, url)

elif action == 'addItem':
    from resources.lib.sources import sources
    sources().addItem(title)

elif action == 'playItem':
   from resources.lib.sources import sources
   sources().playItem(title, source)

elif action == 'alterSources':
    from resources.lib.sources import sources
    sources().alterSources(url, meta)

elif action == 'clearSources':
    from resources.lib.sources import sources
    sources().clearSources()
	
elif action == 'clearMeta':
    import os
    from resources.lib.modules import control
    control.idle()
    try: os.remove(control.cacheFile)
    except:pass
    try: os.remove(control.metacacheFile)
    except:pass
			
    control.infoDialog('Meta Cache Deleted', sound=True, icon='INFO')

elif action == 'backupSettings':
	from resources.lib.modules import updater
	updater.backupAddon()
	
elif action == 'restoreSettings':
	from resources.lib.modules import updater
	updater.restoreAddon()


		
	
	
