import AppLogo from '../atoms/appLogo';
import SplashContainer from '../atoms/splashContainer';
import SplashText from '../atoms/splashText';

const TSplash = ({name}: {name: string}) => {
  return (
    <>
      <SplashContainer>
        <AppLogo />
        <SplashText>{name}</SplashText>
      </SplashContainer>
    </>
  );
};

export default TSplash;
