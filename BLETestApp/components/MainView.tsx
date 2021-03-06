import React from 'react';
import { StyleSheet, View } from 'react-native';
import { Toolbar} from 'react-native-material-ui';
import ScanningButton from './ScanningButton';
import ServicesList from './ServicesList';

const MainView = () => {

  return (
        <View style={styles.container}>
          <Toolbar centerElement="BLE Test App" />
          <ServicesList />
          <ScanningButton />
        </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 15,
  },
});

export default MainView;