import Config from '../../../app.json';
import TSplash from '../templates/splash';

const Splash = () => {
  return (
    <>
      <TSplash name={Config.displayName} />
    </>
  );
};

export default Splash;
