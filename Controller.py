#!/usr/bin/python

import threading
import re
import logging

class Controller(threading.Thread):

    def __init__(self, threads):
        super(Controller, self).__init__()
        self.threads = threads

    def run(self):
    
        logging.info("Starting timer and clock threads")
        for thread in self.threads:
            thread.start()
    
        logging.info("Entering control console")
        while(True):
            cmd = raw_input('rt > ')
        
            logging.info("Got: {0}".format(cmd))
            matches = re.match('([psre]|(?:pause|stop|reset|exit))(\d+)?', cmd)
            
            logging.info("Matches: {0}, {1}".format(matches.group(1), matches.group(2)))
            
            if(not matches):
                print('Invalid command. Valid operators are (p)ause, (r)eset, or (s)top followed by the thread number or (e)xit')
                continue
                 
            elif(matches.group(1) == 'p' or matches.group(1) == 'pause'):
                logging.info("Processing pause")
                
                if(not int(matches.group(2))):
                    print('Invalid thread. Please specify a number between 1 and {0}'.format(self.threads.length))
                    continue
                    
                thr = int(matches.group(2))
                
                if(self.threads[thr].pause.isSet()):
                    self.threads[thr].pause.clear()
                else:
                    self.threads[thr].pause.set()
                
                continue
                
            elif(matches.group(1) == 'r' or matches.group(1) == 'reset'):
                logging.info("Processing reset")
                
                if(not int(matches.group(2))):
                    print('Invalid thread. Please specify a number between 1 and {0}'.format(self.threads.length))
                    continue
                
                thr = int(matches.group(2))
                
                self.threads[thr].reset()
                continue
                
            elif(matches.group(1) == 's' or matches.group(1) == 'stop'):
                logging.info("Processing stop")
                
                if(not int(matches.group(2))):
                    print('Invalid thread. Please specify a number between 1 and {0}'.format(self.threads.length))
                    continue
                                                        
                thr = int(matches.group(2))
                
                self.threads[thr].stop.set()
                continue                

            elif(matches.group(1) == 'e' or matches.group(1) == 'exit'):
                logging.info("Processing exit")
                
                for thread in self.threads:
                    thread.stop.set()
                    
                return True

            else:
                logging.warning("Error processing input")
                continue
                
            return True
                
        return True
