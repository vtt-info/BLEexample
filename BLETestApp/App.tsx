import React, {useEffect, createContext} from 'react';
import {NativeEventEmitter, NativeModules} from 'react-native';
import { ThemeContext, getTheme, COLOR } from 'react-native-material-ui';
import MainView from './components/MainView';
import BleManager from 'react-native-ble-manager';

const BleManagerModule = NativeModules.BleManager;
const bleManagerEmitter = new NativeEventEmitter(BleManagerModule);

export const EmitterContext = createContext(bleManagerEmitter)

const uiTheme = {
  palette: {
    primaryColor: COLOR.green400,
  },
};

const App = ({emitter}) => {

  useEffect(() => {BleManager.start()
                        .then(() => {
                             // Success code
                             console.log('BLE support module initialized');
                           });
                   emitter.addListener('BleManagerDiscoverPeripheral', () => {});
                   emitter.addListener('BleManagerStopScan', () => {});
                   emitter.addListener('BleManagerConnectPeripheral', () => {});
                   emitter.addListener('BleManagerDisconnectPeripheral', () => {});
                   }, []);


  return (
      <EmitterContext.Provider value={emitter}>
           <ThemeContext.Provider value={getTheme(uiTheme)}>
              <MainView />
           </ThemeContext.Provider>
       </EmitterContext.Provider>
  );
}

App.defaultProps = {
    emitter: bleManagerEmitter,
}

export default App;