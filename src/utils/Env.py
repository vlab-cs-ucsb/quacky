# -*- coding: utf-8 -*-
"""
Created on Sat Aug  2 20:21:33 2014


@author: baki
"""
import os
import glob

class Env:
    ######################################################################################
    ####### FUNCTIONS ####################################################################
    ######################################################################################
    @staticmethod
    def get_basename(name):
        return os.path.basename(name)
     
    @staticmethod
    def get_dirname(name):
        return os.path.dirname(name)
        
    @staticmethod
    def join_path(base, name):
        return os.path.join(base,name)
    
    @staticmethod
    def get_abspath(name):
        return os.path.abspath(name)
    
    @staticmethod
    def __get_path(folder='', prefix='', name='', ext=''):
        return os.path.abspath(Env.join_path(folder, prefix + Env.get_basename(name))) + '.' + ext
            
    @staticmethod
    def get_output_file_path(folder, name, ext=''):
        return Env.__get_path(folder=folder, name=name, ext=ext)


         
        
    ######################################################################################
    ####### TEMPORARY VARS ########################################################
    ######################################################################################
    
    # no temp vars
   
