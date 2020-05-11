import React from 'react';
import { StyleSheet, View } from 'react-native';
import { Toolbar} from 'react-native-material-ui';
import ScanningButton from './ScanningButton'

const MainView = () => {

  return (
        <View style={styles.container}>
          <Toolbar style={{ container: { marginTop: 25 } }} centerElement="BLE Test App" />
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
  },
});

export default MainView;