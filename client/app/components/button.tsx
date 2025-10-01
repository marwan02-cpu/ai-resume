'use client'

import {Button} from '@heroui/button';
function PrimaryButton({ action }){
    return (
    <Button className='self-center px-6 py-3 rounded-xl text-white font-semibold
               bg-gradient-to-r from-teal-400 via-sky-500 to-purple-500
               hover:from-teal-500 hover:via-sky-600 hover:to-purple-600
               shadow-md hover:shadow-lg transition' onPress={action}>
      Tailor resume
    </Button>
    )
}

export default PrimaryButton;