import Config from '../../../app.json';
import SplashContainer from '../atoms/splashContainer';
import SplashText from '../atoms/splashText';
import {Image} from 'react-native';

const TSplash = () => {
  return (
    <>
      <SplashContainer>
        <Image source={require('../../assets/images/chef_hat.png')} />
        <SplashText>{Config.displayName}</SplashText>
      </SplashContainer>
    </>
  );
};

export default TSplash;
