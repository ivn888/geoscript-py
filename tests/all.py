import sys
from os import path

sys.path.insert(0,path.join(path.dirname(__file__),path.pardir))

import unittest
import doctest
import geomtest
import projtest
import featuretest
from geoscript import geom, proj, feature

loader = unittest.TestLoader()
runner = unittest.TextTestRunner(verbosity=2)

runner.run(doctest.DocTestSuite(geom))
runner.run(loader.loadTestsFromTestCase(geomtest.GeomTest))
runner.run(doctest.DocTestSuite(proj))
runner.run(loader.loadTestsFromTestCase(projtest.ProjTest))
runner.run(doctest.DocTestSuite(feature))
runner.run(loader.loadTestsFromTestCase(featuretest.FeatureTest))
