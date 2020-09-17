import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import UserProfile103210Navigator from '../features/UserProfile103210/navigator';
import Tutorial103209Navigator from '../features/Tutorial103209/navigator';
import NotificationList103181Navigator from '../features/NotificationList103181/navigator';
import Settings103180Navigator from '../features/Settings103180/navigator';
import Settings103172Navigator from '../features/Settings103172/navigator';
import UserProfile103170Navigator from '../features/UserProfile103170/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {

    //@BlueprintNavigationInsertion
UserProfile103210: { screen: UserProfile103210Navigator },
Tutorial103209: { screen: Tutorial103209Navigator },
NotificationList103181: { screen: NotificationList103181Navigator },
Settings103180: { screen: Settings103180Navigator },
Settings103172: { screen: Settings103172Navigator },
UserProfile103170: { screen: UserProfile103170Navigator },

    /** new navigators can be added here */
    SplashScreen: {
      screen: SplashScreen
    }
};

const DrawerAppNavigator = createDrawerNavigator(
  {
    ...AppNavigator,
  },
  {
    contentComponent: SideMenu
  },
);

const AppContainer = createAppContainer(DrawerAppNavigator);

export default AppContainer;
