import Svg, {Path} from 'react-native-svg';

function AppLogo(props) {
  return (
    <Svg
      fill="#FFFF"
      height={`${props?.height || 160}px`}
      viewBox="0 0 463 463"
      width={`${props?.width || 160}px`}
      xmlns="http://www.w3.org/2000/svg"
      xmlSpace="preserve"
      {...props}>
      <Path d="M367.5 116c-14.435 0-28.741 3.323-41.735 9.655-19.933-21.896-46.566-35.999-75.529-40.273l-.023-.003a128 128 0 00-4.52-.586l-.135-.016a130.218 130.218 0 00-4.475-.414c-.185-.014-.37-.023-.555-.036a128.846 128.846 0 00-3.687-.205c-.361-.015-.722-.03-1.084-.042-1.416-.048-2.834-.08-4.257-.08-1.423 0-2.841.032-4.257.079-.362.012-.723.027-1.084.042-1.232.051-2.461.119-3.687.205-.185.013-.371.022-.555.036-1.497.112-2.988.251-4.475.414l-.135.016a128 128 0 00-4.52.586l-.023.003c-28.963 4.274-55.596 18.376-75.529 40.273-12.994-6.331-27.3-9.654-41.735-9.654C42.841 116 0 158.841 0 211.5c0 34.256 18.584 65.836 48 82.75v61.25c0 12.958 10.542 23.5 23.5 23.5h320c12.958 0 23.5-10.542 23.5-23.5v-61.25c29.416-16.914 48-48.494 48-82.75 0-52.659-42.841-95.5-95.5-95.5zm-104 248h-64c-9.098 0-16.5-7.402-16.5-16.5 0-9.098 7.402-16.5 16.5-16.5h64c9.098 0 16.5 7.402 16.5 16.5 0 9.098-7.402 16.5-16.5 16.5zm136.5-8.5c0 4.687-3.813 8.5-8.5 8.5H290.319A31.31 31.31 0 00295 347.5c0-17.369-14.131-31.5-31.5-31.5h-64c-17.369 0-31.5 14.131-31.5 31.5a31.31 31.31 0 004.681 16.5H71.5c-4.687 0-8.5-3.813-8.5-8.5V299h337v56.5zm2.303-71.5h-65.915a127.503 127.503 0 007.903-12.996 7.5 7.5 0 00-13.262-7.01 112.803 112.803 0 01-13.504 20.005H145.476a112.75 112.75 0 01-13.504-20.005 7.5 7.5 0 00-10.136-3.126 7.5 7.5 0 00-3.126 10.135 127.503 127.503 0 007.903 12.996H60.697C32.889 270.625 15 242.347 15 211.5c0-44.388 36.112-80.5 80.5-80.5 11.028 0 21.966 2.313 32.077 6.724a127.75 127.75 0 00-12.897 22.771 7.5 7.5 0 0013.744 6.01c15.687-35.879 48.621-60.649 86.543-66.285a111.694 111.694 0 017.895-.883c.283-.022.567-.04.851-.059a112.87 112.87 0 012.976-.166c.341-.014.682-.031 1.024-.042 1.259-.042 2.521-.07 3.788-.07s2.529.028 3.788.07c.342.011.683.028 1.024.042.995.043 1.987.097 2.976.166.284.02.567.037.851.059a111.694 111.694 0 017.895.883c37.922 5.635 70.856 30.406 86.543 66.285a7.502 7.502 0 006.876 4.497 7.502 7.502 0 006.868-10.507 127.75 127.75 0 00-12.897-22.771c10.112-4.411 21.05-6.724 32.077-6.724 44.388 0 80.5 36.112 80.5 80.5-.002 30.847-17.891 59.125-45.699 72.5z" />
    </Svg>
  );
}

export default AppLogo;
