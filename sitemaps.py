import sys
import logging
from pysitemap import crawler


if __name__ == '__main__':
    if '--iocp' in sys.argv:
        from asyncio import events, windows_events
        sys.argv.remove('--iocp')
        logging.info('using iocp')
        el = windows_events.ProactorEventLoop()
        events.set_event_loop(el)
        
root_url = 'https://www.glamira.com/'
crawler(root_url, out_file='sitemap.xml')