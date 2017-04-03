import arcpy
import os
import shutil
import logging
import logging.config
import datetime
from datetime import datetime

# Setup the logfile name
t = datetime.now()
logFile = "Z:/ScriptsForArcGIS/ArcSDE_ShapeFile/Logs/"
logName = logFile + t.strftime("%y%m%d") + ".log"
# Setup logging
logger = logging.getLogger("shape_file_creation")
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(logName)
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(filename)s : line %(lineno)d - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

try:

        for root, dirs, files in os.walk('//fspw/Apps/GIS_Data/Utilities_SDE_Maps/Water'):
                for f in files:
                        os.unlink(os.path.join(root, f))
                for d in dirs:
                        shutil.rmtree(os.path.join(root, d))

        print "Water folder shapefiles successfully deleted."
	logger.info("Water folder shapefiles successfully deleted.")
	
        for root, dirs, files in os.walk('//fspw/Apps/GIS_Data/Utilities_SDE_Maps/Storm'):
                for f in files:
                    os.unlink(os.path.join(root, f))
                for d in dirs:
                    shutil.rmtree(os.path.join(root, d))
                    
        print "Storm folder shapefiles successfully deleted."
	logger.info("Storm folder shapefiles successfully deleted.")

        for root, dirs, files in os.walk('//fspw/Apps/GIS_Data/Utilities_SDE_Maps/Sanitary'):
                for f in files:
                    os.unlink(os.path.join(root, f))
                for d in dirs:
                    shutil.rmtree(os.path.join(root, d))

        print "Sanitary folder shapefiles successfully deleted."
	logger.info("Sanitary folder shapefiles successfully deleted.")
	
        #Output folders
        Water = "//fspw/Apps/GIS_Data/Utilities_SDE_Maps/Water"
        Storm = "//fspw/Apps/GIS_Data/Utilities_SDE_Maps/Storm"
        Sanitary = "//fspw/Apps/GIS_Data/Utilities_SDE_Maps/Sanitary"

        arcpy.FeatureClassToShapefile_conversion("'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WATER_NETWORK\\OPERATIONS.OPS.wWaterDistrict';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WATER_NETWORK\\OPERATIONS.OPS.wVaultDrain';''C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WATER_NETWORK\\OPERATIONS.OPS.wVault';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WATER_NETWORK\\OPERATIONS.OPS.wTank';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WATER_NETWORK\\OPERATIONS.OPS.wSystemValve';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WATER_NETWORK\\OPERATIONS.OPS.wPumpStation';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WATER_NETWORK\\OPERATIONS.OPS.wPump';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WATER_NETWORK\\OPERATIONS.OPS.wPressureZone';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WATER_NETWORK\\OPERATIONS.OPS.wOmniBall';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WATER_NETWORK\\OPERATIONS.OPS.wNetworkStructure';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WATER_NETWORK\\OPERATIONS.OPS.wMasterMeter';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WATER_NETWORK\\OPERATIONS.OPS.wMain';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WATER_NETWORK\\OPERATIONS.OPS.wLateralLine';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WATER_NETWORK\\OPERATIONS.OPS.wJunctionBox';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WATER_NETWORK\\OPERATIONS.OPS.wHydrant';''C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WATER_NETWORK\\OPERATIONS.OPS.wFitting';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WATER_NETWORK\\OPERATIONS.OPS.wCPWires';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WATER_NETWORK\\OPERATIONS.OPS.wControlValve';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WATER_NETWORK\\OPERATIONS.OPS.wCasing';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WATER_NETWORK\\OPERATIONS.OPS.wAirVac'", Water)
        arcpy.FeatureClassToShapefile_conversion("'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.STORM_NETWORK\\OPERATIONS.OPS.swCasing';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.STORM_NETWORK\\OPERATIONS.OPS.swCeptor';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.STORM_NETWORK\\OPERATIONS.OPS.swCleanOut';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.STORM_NETWORK\\OPERATIONS.OPS.swControlValve';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.STORM_NETWORK\\OPERATIONS.OPS.swCreeks';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.STORM_NETWORK\\OPERATIONS.OPS.swCulverts';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.STORM_NETWORK\\OPERATIONS.OPS.swDetentionPond';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.STORM_NETWORK\\OPERATIONS.OPS.swFitting';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.STORM_NETWORK\\OPERATIONS.OPS.swGravityMain';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.STORM_NETWORK\\OPERATIONS.OPS.swInlet';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.STORM_NETWORK\\OPERATIONS.OPS.swIrrigationDitch';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.STORM_NETWORK\\OPERATIONS.OPS.swIrrigationPipe';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.STORM_NETWORK\\OPERATIONS.OPS.swManhole';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.STORM_NETWORK\\OPERATIONS.OPS.swNetworkLine';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.STORM_NETWORK\\OPERATIONS.OPS.swNetworkStructure';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.STORM_NETWORK\\OPERATIONS.OPS.swOpenDrain';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.STORM_NETWORK\\OPERATIONS.OPS.swOutfall';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.STORM_NETWORK\\OPERATIONS.OPS.swPipeEnd';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.STORM_NETWORK\\OPERATIONS.OPS.swStormMain';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.STORM_NETWORK\\OPERATIONS.OPS.swUnderDrain'", Storm)
        arcpy.FeatureClassToShapefile_conversion("'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WASTEWATER_NETWORK\\OPERATIONS.OPS.ssAssetGroups';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WASTEWATER_NETWORK\\OPERATIONS.OPS.ssCasing';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WASTEWATER_NETWORK\\OPERATIONS.OPS.ssCleanOut';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WASTEWATER_NETWORK\\OPERATIONS.OPS.ssFitting';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WASTEWATER_NETWORK\\OPERATIONS.OPS.ssGravityMain';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WASTEWATER_NETWORK\\OPERATIONS.OPS.ssGreaseTraps';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WASTEWATER_NETWORK\\OPERATIONS.OPS.ssLateralLine';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WASTEWATER_NETWORK\\OPERATIONS.OPS.ssLiftStation';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WASTEWATER_NETWORK\\OPERATIONS.OPS.ssManhole';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WASTEWATER_NETWORK\\OPERATIONS.OPS.ssMeterStation';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WASTEWATER_NETWORK\\OPERATIONS.OPS.ssNetworkStructure';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WASTEWATER_NETWORK\\OPERATIONS.OPS.ssPressurizedMain';'C:\\ScriptsForArcGIS\\ArcSDE_ShapeFile\\OPERATIONS - OPSVIEW.sde\\OPERATIONS.OPS.WASTEWATER_NETWORK\\OPERATIONS.OPS.ssPump'", Sanitary)

        print "Water, Storm and Sanitary Network Shapefiles have been rebuilt"
        print "Process complete!"
	logger.info("Water, Storm and Sanitary Network Shapefiles have been rebuilt")
	logger.info ("Process complete!")

except Exception as e:
	print e.args[0]
	import smtplib

	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText

        # Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Python Script Failed - SDE to SHP Export broken"
	msg['From'] = "maps@arvada.org"
	msg['To'] = "ghumphries@arvada.org"

        # Create the body of the message (an HTML version).
	text = "Hey,\n\nBad news dude. You've got some work to do. The Python script that creates Shapefiles from SDE for the CAD group tossed an error.\n\nThe failed script was: \
ArcSDE_To_SHP.py\n\nThe error is:  " + str(e) + "\n\n"

        # Record the MIME types of both parts - text/plain and text/html.
	part1 = MIMEText(text, 'plain')

        # Attach parts into message container.
	msg.attach(part1)

        # Send the message via local SMTP server.
	s = smtplib.SMTP('10.10.1.100')
        # sendmail function takes 3 arguments: sender's parceless, recipient's parceless
        # and message to send - here it is sent as one string.
	s.sendmail(msg['From'], msg['To'].split(","), msg.as_string())
	s.quit()
	logger.exception(str(e))
except arcpy.ExecuteError:
	print arcpy.GetMessages(2)

logging.shutdown()


