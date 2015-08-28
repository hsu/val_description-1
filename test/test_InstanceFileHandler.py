#!/usr/bin/env python

import unittest
import os
from val_description.InstanceFileHandler import InstanceFileHandler
import xml.etree.ElementTree as xmlParser


class instanceFileHandlerTests(unittest.TestCase):

    def setUp(self):
        self.testDirectory = os.path.dirname(os.path.abspath(__file__))

    def tearDown(self):
        pass

    def testGetXmlRoot(self):
        sampleInstanceFile = self.testDirectory + '/test_files/valkyrie_A.xml'
        instanceFileHandler = InstanceFileHandler(sampleInstanceFile)
        assert instanceFileHandler.getInstanceRoot().tag == 'robot'

    def testGetMechanisms(self):
        sampleInstanceFile = self.testDirectory + '/test_files/valkyrie_A.xml'
        instanceFileHandler = InstanceFileHandler(sampleInstanceFile)
        mechanisms = instanceFileHandler.getMechanisms()
        mechanism_ids = ['left_hip_yaw', 'left_hip_roll', 'left_hip_pitch', 'left_knee_pitch', 'left_ankle',
                         'right_hip_yaw', 'right_hip_roll', 'right_hip_pitch', 'right_knee_pitch', 'right_ankle',
                         'left_shoulder_pitch', 'left_shoulder_roll', 'left_shoulder_yaw', 'left_elbow_pitch',
                         'left_forearm_yaw', 'left_wrist', 'right_shoulder_pitch', 'right_shoulder_roll',
                         'right_shoulder_yaw', 'right_elbow_pitch', 'right_forearm_yaw', 'right_wrist',
                         'lower_neck_pitch', 'neck_yaw', 'upper_neck_pitch', 'torso_yaw', 'waist']
        for mechanism in mechanisms:
            assert mechanism.tag == 'Mechanism'
            assert mechanism.get('id') in mechanism_ids

    def testGetChannels(self):
        sampleInstanceFile = self.testDirectory + '/test_files/valkyrie_A.xml'
        instanceFileHandler = InstanceFileHandler(sampleInstanceFile)
        channels = instanceFileHandler.getChannels()
        channelsToCheck = [
            '/right_arm', '/left_arm', '/right_leg', '/left_leg', '/neck', '/trunk']
        for channel in channels:
            assert channel.tag == 'Channel'
            assert channel.get('id') in channelsToCheck

    def testGetDevices(self):
        sampleInstanceFile = self.testDirectory + '/test_files/valkyrie_A.xml'
        instanceFileHandler = InstanceFileHandler(sampleInstanceFile)
        devices = instanceFileHandler.getDevices()
        devicesToCheck = ['pelvis_imu1', 'pelvis_imu2', 'torso_imu1',
                          'torso_imu2', 'left_foot_force_torque', 'right_foot_force_torque']
        for device in devices:
            assert device.tag == 'Device'
            assert device.get('id') in devicesToCheck

    def testGetActuatorSerialNumbers(self):
        sampleInstanceFile = self.testDirectory + '/test_files/valkyrie_A.xml'
        instanceFileHandler = InstanceFileHandler(sampleInstanceFile)
        serialNumbers = instanceFileHandler.getSerialNumbers()
        serialNumbersToCheck = ['v_a_001', 'v_b_001', 'v_c_001', 'v_d_001', 'v_e_001', 'v_e_002', 'v_a_002', 'v_b_002', 'v_c_002',
                                'v_d_002', 'v_e_003', 'v_e_004', 'v_a_003', 'v_b_003', 'v_f_001', 'v_f_001', 'v_g_001', 'v_e_001',
                                'v_e_002', 'v_a_004', 'v_b_004', 'v_f_002', 'v_f_002', 'v_g_002', 'v_e_003', 'v_e_004', 'v_g_001',
                                'v_g_001', 'v_g_001', 'v_a_005', 'v_e_005', 'v_e_006']

        for serialNumber in serialNumbers:
            assert serialNumber in serialNumbersToCheck

    def testGetActuatorCoeffFiles(self):
        sampleInstanceFile = self.testDirectory + '/test_files/valkyrie_A.xml'
        instanceFileHandler = InstanceFileHandler(sampleInstanceFile)
        coeffFiles = instanceFileHandler.getActuatorCoeffFiles()
        coeffFilesToCheck = ['v_a_001.xml', 'v_b_001.xml', 'v_c_001.xml', 'v_d_001.xml', 'v_e_001.xml', 'v_e_002.xml', 'v_a_002.xml', 'v_b_002.xml', 'v_c_002.xml',
                             'v_d_002.xml', 'v_e_003.xml', 'v_e_004.xml', 'v_a_003.xml', 'v_b_003.xml', 'v_f_001.xml', 'v_f_001.xml', 'v_g_001.xml', 'v_e_001.xml',
                             'v_e_002.xml', 'v_a_004.xml', 'v_b_004.xml', 'v_f_002.xml', 'v_f_002.xml', 'v_g_002.xml', 'v_e_003.xml', 'v_e_004.xml', 'v_g_001.xml',
                             'v_g_001.xml', 'v_g_001.xml', 'v_a_005.xml', 'v_e_005.xml', 'v_e_006.xml']

        for coeffFile in coeffFiles:
            assert coeffFile in coeffFilesToCheck

    def testGetActuatorSerialNumberByNode(self):
        sampleInstanceFile = self.testDirectory + '/test_files/valkyrie_A.xml'
        instanceFileHandler = InstanceFileHandler(sampleInstanceFile)
        node = '/left_leg/j4'
        serialNumberToCheck = 'v_d_001'
        serialNumber = instanceFileHandler.getActuatorSerialNumberByNode(node)

        assert serialNumber == serialNumberToCheck

        node = '/left_leg/ankle/actuator0'
        serialNumberToCheck = 'v_e_001'
        serialNumber = instanceFileHandler.getActuatorSerialNumberByNode(node)

        assert serialNumber == serialNumberToCheck

    def testGetNodes(self):
        sampleInstanceFile = self.testDirectory + '/test_files/valkyrie_A.xml'
        instanceFileHandler = InstanceFileHandler(sampleInstanceFile)
        nodes = instanceFileHandler.getNodes()
        nodesToCheck = ['/left_leg/j1', '/left_leg/j2', '/left_leg/j3', '/left_leg/j4',
                        '/left_leg/ankle/actuator0', '/left_leg/ankle/actuator1', '/right_leg/j1', '/right_leg/j2',
                        '/right_leg/j3', '/right_leg/j4', '/right_leg/ankle/actuator0', '/right_leg/ankle/actuator1',
                        '/left_arm/j1', '/left_arm/j2', '/left_arm/j3', '/left_arm/j4', '/left_arm/j4',
                        '/left_leg/ankle/actuator0', '/left_leg/ankle/actuator1', '/right_arm/j1', '/right_arm/j2',
                        '/right_arm/j3', '/right_arm/j4', '/right_arm/j4', '/right_leg/ankle/actuator0',
                        '/right_leg/ankle/actuator1', '/neck/j1', '/neck/j2', '/neck/j3', '/trunk/j1',
                        '/trunk/waist/actuator0', '/trunk/waist/actuator1']

        for node in nodes:
            assert node in nodesToCheck

    def testInstanceConfigDictionary(self):
        sampleInstanceFile = self.testDirectory + \
            '/test_files/sample_instance.xml'
        instanceFileHandler = InstanceFileHandler(sampleInstanceFile)

        expectedConfigDictionary = {'/left_leg/j1': {'configFiles': ['v_a_001.xml', 'a.xml', 'a_sv.xml',
                                                                     'sensors.xml', 'safety.xml', 'mode.xml'], 'firmware': 'rotary/turbo_bootloader.bin', 'type': 'turbodriver',
                                                     'location': '/left_leg/j1'}, '/left_leg/ankle/actuator1': {'configFiles': ['v_e_002.xml', 'e.xml',
                                                                                                                                'e_sv.xml', 'sensors.xml', 'safety.xml', 'mode.xml'], 'firmware': 'linear/turbo_bootloader.bin',
                                                                                                                'type': 'turbodriver', 'location': '/left_leg/ankle/actuator1'}}

        instanceConfig = instanceFileHandler.getInstanceConfig()

        assert cmp(instanceConfig, expectedConfigDictionary) == 0

    def testGetFirmwareType(self):
        sampleInstanceFile = self.testDirectory + \
            '/test_files/sample_instance.xml'
        instanceFileHandler = InstanceFileHandler(sampleInstanceFile)

        expectedFirmwareType = 'rotary/turbo_bootloader.bin'
        firmwareType = instanceFileHandler.getFirmwareType('/left_leg/j1')

        assert firmwareType == expectedFirmwareType

    def testGetNodeType(self):
        sampleInstanceFile = self.testDirectory + \
            '/test_files/sample_instance.xml'
        instanceFileHandler = InstanceFileHandler(sampleInstanceFile)

        expectedNodeType = 'turbodriver'
        nodeType = instanceFileHandler.getNodeType('/left_leg/j1')

        assert nodeType == expectedNodeType

    def testGatherCoeffs(self):
        sampleInstanceFile = self.testDirectory + \
            '/test_files/sample_instance.xml'
        instanceFileHandler = InstanceFileHandler(sampleInstanceFile)

        coeffs = instanceFileHandler.gatherCoeffs("/left_leg/j1")
        expectedCoeffs = {'TemperatureSensor_SensorLoc2': 2.0, 'TemperatureSensor_SensorLoc1': 1.0, 'JointSensors_OutputPosition': 2.0,
                          'IGainAmpsPerBit': 0.018928, 'DeltaAPSSafeLimit': 9999.0, 'TorqueControl_enablePID': 1.0,
                          'TorqueControl_FFd_fc_Hz': 25.0, 'APS1DriftSafeLimit': 9999.0, 'PositionControl_MotorTorqueDirection': 1.0,
                          'TorqueControl_Kd_fc_Hz': 50.0, 'VelocitySafeLimit': 9999.0, 'WindingResistance': 2.112, 'JointOutputAPS_MountingGain': 1.0,
                          'JointSafety_LowerLimit_Rad': -1.6, 'CommTimeoutMs': 80.0, 'PhaseACurOffset': 2048.0, 'JerkSafeLimit': 9999.0,
                          'BusVoltage_SensorGain': 0.163412, 'PositionOffset_Rad': -1.6651, 'EncMountingDir': 1.0, 'TorqueControl_TdobWindupLimit_Nm': 80.0,
                          'MotorAccFilter_fc_Hz': 50.0, 'JointOutputAPS_CountsToRad': 0.00076699038, 'PhaseCCurOffset': 2045.0, 'SpaceVector_MaxNormVoltage': 0.666,
                          'MotorWindingType': 0.0, 'TorqueControl_Tdob_fc_Hz': 50.0, 'JointSensors_OutputVelocity': 1.0, 'Renishaw_CountsToRad': 5.8516723e-09,
                          'TorqueControl_m': 1.2, 'EncoderIndexOffset': 1.16973095726, 'BusVoltage_BitOffset': 2048.0, 'SpringStiffness': 2750.0,
                          'Inductance_DAxis': 0.0009, 'MotorVelFilter_fc_Hz': 800.0, 'JointKinematicDir': -1.0, 'TorqueOffset_Nm': -9.39, 'TemperatureSensor_MaxTemp1': 125.0,
                          'TorqueControl_MotorTorqueDirection': 1.0, 'TemperatureSensor_MaxTemp2': 110.0, 'PositionControl_Kd': 1.0, 'TorqueControl_Current2MotorTorque': 0.0375,
                          'PhaseBCurOffset': 2048.0, 'TorqueControl_PD_damp': 0.95, 'EncDriftSafeLimit': 9999.0, 'DeadTimeCompensation': 0.02, 'TorqueControl_b': 70.0, 'TorqueControl_enableDOB': 1.0,
                          'SpringAPS_MountingGain': -1.0, 'PositionControl_Kd_fc_Hz': 50.0, 'Inductance_QAxis': 0.00139, 'JointVelFilter_fc_Hz': 30.0,
                          'PositionControl_Kp': 500.0, 'TorqueControl_enableFF': 1.0, 'JointGearRatio': 160.0, 'NumberOfPoles': 8.0, 'PositionControl_SensorFeedback': 4.0,
                          'PositionControl_Input_fc_Hz': 30.0, 'JointMinValue': -3.14159265359, 'FluxLinkage': 0.0444, 'TorqueControl_Kd': 0.0, 'JointTorqueLimit_Nm': 190.0,
                          'TorqueControl_Kp': 0.0, 'SpringAPS_BitOffset': 115108200.0, 'JointSensors_MotorPosition': 1.0, 'JointSafety_LimitZone_Rad': 0.07,
                          'TorqueControl_enableDynFF': 0.0, 'TorqueControl_autoKd': 1.0, 'JointSensors_OutputForce': 2.0, 'PositionControl_enableInLPF': 1.0,
                          'Commutation_Select': 2.0, 'JointMaxValue': 3.14159265359, 'CurrVelFilter_fc_Hz': 200.0, 'TorqueControl_ParallelDamping': 0.0, 'JointSafety_UpperLimit_Rad': 1.6,
                          'EncoderCPR': 544.0, 'SpaceVector_CurrentToSV': 1.0, 'CurrentSafeLimit': 13.0}

        assert cmp(coeffs, expectedCoeffs) == 0

    def testLoadXMLCoeffs(self):
        sampleInstanceFile = self.testDirectory + \
            '/test_files/sample_instance.xml'
        instanceFileHandler = InstanceFileHandler(sampleInstanceFile)

        expectedCoeffs = {'JointSafety_LowerLimit_Rad': {'source': 'v_a_001.xml', 'value': -1.6},
                          'JointSensors_OutputPosition': {'source': 'v_a_001.xml', 'value': 2.0},
                          'PositionControl_MotorTorqueDirection': {'source': 'v_a_001.xml', 'value': 1.0},
                          'JointOutputAPS_MountingGain': {'source': 'v_a_001.xml', 'value': 1.0},
                          'SpringAPS_MountingGain': {'source': 'v_a_001.xml', 'value': -1.0},
                          'PositionControl_enableInLPF': {'source': 'v_a_001.xml', 'value': 1.0},
                          'PositionOffset_Rad': {'source': 'v_a_001.xml', 'value': -1.6651},
                          'JointSensors_OutputVelocity': {'source': 'v_a_001.xml', 'value': 1.0},
                          'TorqueOffset_Nm': {'source': 'v_a_001.xml', 'value': -9.39},
                          'EncoderIndexOffset': {'source': 'v_a_001.xml', 'value': 1.16973095726},
                          'JointKinematicDir': {'source': 'v_a_001.xml', 'value': -1.0},
                          'TorqueControl_MotorTorqueDirection': {'source': 'v_a_001.xml', 'value': 1.0},
                          'EncMountingDir': {'source': 'v_a_001.xml', 'value': 1.0},
                          'JointMaxValue': {'source': 'v_a_001.xml', 'value': 3.14159265359},
                          'JointSafety_UpperLimit_Rad': {'source': 'v_a_001.xml', 'value': 1.6},
                          'JointSensors_OutputForce': {'source': 'v_a_001.xml', 'value': 2.0},
                          'JointMinValue': {'source': 'v_a_001.xml', 'value': -3.14159265359},
                          'SpringAPS_BitOffset': {'source': 'v_a_001.xml', 'value': 115108200.0},
                          'JointTorqueLimit_Nm': {'source': 'v_a_001.xml', 'value': 190.0},
                          'JointSensors_MotorPosition': {'source': 'v_a_001.xml', 'value': 1.0},
                          'JointSafety_LimitZone_Rad': {'source': 'v_a_001.xml', 'value': 0.07},
                          'PositionControl_Input_fc_Hz': {'source': 'v_a_001.xml', 'value': 30.0}}

        # print instanceFileHandler.loadXMLCoeffs('v_a_001.xml')
        assert cmp(instanceFileHandler.loadXMLCoeffs(
            'v_a_001.xml'), expectedCoeffs) == 0

if __name__ == '__main__':
    unittest.main()
